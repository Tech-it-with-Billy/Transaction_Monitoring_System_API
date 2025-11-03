from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 
                'created_by', 'created_at', 'updated_at', 'account_number', 'account_balance'
                ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at', 'account_balance']
    
    def validate_account_number(self, value):
        if Customer.objects.filter(account_number=value).exists():
            raise serializers.ValidationError('Account already registered!')
        return value
    
    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user
        return super().create(validated_data)