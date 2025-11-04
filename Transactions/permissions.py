from rest_framework.permissions import BasePermission

class RolePermissions(BasePermission):
    allowed_roles = []
    
    def has_permission(self, request, view):
        return (
            request.user and request.user.IsAuthenticated and request.user.role in self.allowed_roles
            )

class IsAdmin(RolePermissions):
    allowed_roles = ['admin']

class IsOperator(RolePermissions):
    allowed_roles = ['operator']

class IsAnalyst(RolePermissions):
    allowed_roles = ['analyst']