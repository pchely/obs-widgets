from rest_framework import serializers
from .models import OBS_Model


class StatusWidget(serializers.ModelSerializer):
    class Meta:
        model = OBS_Model
        fields = ("status",)



class AboutWidget(serializers.ModelSerializer):
    class Meta:
        model = OBS_Model
        fields = ("title","subtitle")
