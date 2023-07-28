from rest_framework import serializers
from django_api.models import User
from rest_framework_simplejwt.tokens import RefreshToken,OutstandingToken



class UserRegisterSerializers(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=["contact","name","email","password","password2"]
        extra_kwargs={
            'password':{'write_only':True}
        }



    #validating password    
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password does not match")
        else:
            return attrs
        

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

#UserLogin
class UserLoginSerializer(serializers.ModelSerializer):
    contact=serializers.CharField(max_length=10)
    class Meta:
        model=User
        fields=["contact","password" ]





#UserLogout

class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except Exception as e:
            raise serializers.ValidationError("Invalid refresh token.")