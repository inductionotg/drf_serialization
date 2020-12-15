from rest_framework import serializers
from testApp.models import Employee
'''Normal Serializer'''
'''class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=64)
    eaddr=serializers.CharField(max_length=64)
    esal=serializers.IntegerField()
    #field level validation
    def validate_esal(self,value):
        if value<5000:
            raise serializers.ValidationError('employees salary should be minimum 5000')
        return value

    #Object level validation
    def validate(self,data):
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower()=='sunny':
            if esal<50000:
                raise serializer.ValidationError('sunny salary should be min 50000')
        return data

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.eno)
        instance.esal=validated_data.get('esal',instance.eno)
        instance.eaddr=validated_data.get('eaddr',instance.eno)
        instance.save()
        return instance
'''


'''Model Serializer'''

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
