from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Livro


class LivroListSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1


class LivroRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1


class LivroSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Livro
        fields = "__all__"
