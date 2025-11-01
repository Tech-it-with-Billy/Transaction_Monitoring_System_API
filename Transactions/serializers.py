from rest_framework import serializers
from .models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            'id', 'reference', 'account_number', 'amount', 
            'transaction_time', 'status', 'customer', 'created_by',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'reference', 'transaction_time', 'customer',
            'created_by', 'created_at', 'updated_at'
        ]
        
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)
        