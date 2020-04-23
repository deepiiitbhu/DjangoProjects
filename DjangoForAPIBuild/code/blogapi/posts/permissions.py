
from rest_framework import permissions

'''
Internally, Django REST Framework relies on a BasePermission class from which all
other permission classes inherit. That means the built-in permissions settings like
AllowAny, IsAuthenticated, and others extend it.

class BasePermission(object):
    """
        A base class from which all permission classes should inherit.
    """
        def has_permission(self, request, view):
            """
            Return `True` if permission is granted, `False` otherwise.
            """
    return True
        def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
    return True

To create our own custom permission, we will override the has_object_permission
method. Specifically we want to allow read-only for all requests but for any write
requests, such as edit or delete, the author must be the same as the current loggedin user.
Here is what our posts/permissions.py file looks like.
'''

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user