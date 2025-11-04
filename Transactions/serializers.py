from rest_framework import serializers
from .models import Transaction
from Customer.models import Customer

class TransactionSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Transaction
        fields = [
            'id', 'reference', 'customer', 'customer_name', 'transaction_type', 'amount',
            'transaction_time', 'status', 'created_by', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'reference', 'transaction_time', 'created_by', 'created_at', 'updated_at']
    
    def get_customer_name(self, obj):
        return f'{obj.customer.first_name} {obj.customer.last_name}'
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Transaction Amount must be greater than ZERO!')
        return value
    
    def validate(self, attrs):
        transaction_type = attrs.get('transaction_type')
        customer = attrs.get('customer')
        amount = attrs.get('amount')
        
        if transaction_type == 'withdrawal':
            if customer.account_balance < amount:
                raise serializers.ValidationError('Insufficient balance for withdrawals!')
            return attrs
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['created_by'] = request.user if request else None
        transaction = Transaction.objects.create(**validated_data)
        
        customer = validated_data['customer']
        if transaction.transaction_type == 'deposit':
            customer.account_balance += transaction.amount
        elif transaction.transaction_type == 'withdrawal':
            customer.account_balance -= transaction.amount
        customer.save()
        
        return transaction