from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from djoser.conf import settings
from .models import *
from friend.serializers import *
from gift.models import Gift,UserGift

# User = get_user_model()

class UserTagSerializar(serializers.ModelSerializer):
    class Meta:
        model = UserTag
        fields = '__all__'


class UserSerializerForGift(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'avatar',
            'fio',
            'nickname',
            'is_online'
        ]

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = '__all__'

class UserGiftSerializer(serializers.ModelSerializer):
    gift = GiftSerializer(many=False)
    from_user = UserSerializerForGift(many=False)
    class Meta:
        model = UserGift
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(read_only=True)
    bg_image = serializers.SerializerMethodField(read_only=True)
    own_friend_list = FriendListSerializer(many=True, required=False,read_only=True)
    # apply_list = FriendApplySerializer(many=True)
    gifts = UserGiftSerializer(many=True, required=False,read_only=True)
    # tags = UserTagSerializar(many=True, required=False,read_only=True)
    years = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields=[
            'id',
            'avatar',
            'bg_image',
            'is_online',
            'fio',
            'nickname',
            # 'wechatid',
            # 'email',
            'birthday',
            'balance',
            'rating',
            'level',
            'years',
            'vip_update',
            'vip_expire',
            'is_vip',
            'is_streamer',
            'is_verified',
            'is_email_verified',
            'own_friend_list',
            # 'apply_list',
            'gifts',
            'streamer_rating',
            'streams_rating',
            'tags',
            'about',
            'city',
            'education',
            'work_place',
            'interests',
            'interests_additional',
            'last_login',
            'date_joined',
            'suid'
        ]

    def get_years(self, obj):
        from datetime import date, timedelta
        if obj.birthday:

            return (date.today() - obj.birthday) // timedelta(days=365.2425)
        else:
            return None

    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        else:
            return '/no-avatar.svg'

    def get_bg_image(self, obj):
        if obj.bg_image:
            return self.context['request'].build_absolute_uri(obj.bg_image.image.url)
        else:
            return '/test-user-profile-bg.png'




class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR
    }

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            User._meta.pk.name,
            "password",
            'fio',
            'wechatid',
            'email',
            'nickname'

        )

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        # print(validated_data)
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        # print('validated_data',validated_data)
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user


class UserBgSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBg
        fields = '__all__'
