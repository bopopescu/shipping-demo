from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from apps.areas.models import ServiceArea


def user_is_provider(user):
    return hasattr(user, 'provider')


class IsAuthorized(BasePermission):
    """
    This permission implements the following semantic:
     - All users can read areas.
     - Only Providers can create areas.
     - Only the owner of an area can modify/delete such area.
    """

    def has_permission(self, request, view):
        # Read allowed for everyone
        if request.method in SAFE_METHODS:
            return True

        # Past this point, we only allow Providers
        if not user_is_provider(request.user):
            return False

        # All providers can create new areas
        if request.method == "POST":
            return True

        # This is a patch/delete request, so we must
        # check that request user is owner of this area
        return ServiceArea.objects.filter(
            pk=view.kwargs['pk'],
            provider__user_id=request.user.id,
        ).exists()
