from rest_framework import serializers
from users.models import User,VideoLike
from videos.serializers import VideoSerializer,BodyPartSerializer

class UserSerializer(serializers.ModelSerializer): 
    userlikes_num = serializers.SerializerMethodField()
    
    recent_video = VideoSerializer(required=False)
    bodypart = BodyPartSerializer(many=True)

    class Meta:
        model = User
        fields = ['id','username','password','email','recent_video','bodypart','userlikes_num','fullname']
        extra_kwargs = {'password':{'write_only':True}}

    def get_userlikes_num(self,obj): 
        return VideoLike.objects.filter(user=obj).count()

class VideoLikeSerializer(serializers.ModelSerializer):
      video = VideoSerializer()
      user = UserSerializer()

      class Meta:
          model = VideoLike
          fields = ['id','video','user']

    

