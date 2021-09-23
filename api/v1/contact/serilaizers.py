from contact.models import Contact, EmailAccount, PhoneDetail
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class ContactSerializer(serializers.ModelSerializer):
    emails = serializers.SerializerMethodField()
    phones = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = "__all__"
        read_only = ("id",)
        extra_kwargs = {
            "mid_name": {
                "required": True,
            }
        }

    def get_emails(self, *args, **kwargs):
        contact = args[0]
        eas = EmailAccount.objects.filter(contact_id=contact.id)
        serializer = EmailAccountSerializer(instance=eas, many=True)
        return serializer.data
        # eas = eas.values_list("email", flat=True)
        # return list(eas)

    def get_phones(self, *args, **kwargs):
        contact = args[0]
        ps = PhoneDetail.objects.filter(contact_id=contact.id)
        serializer = PhoneDetailSerializer(instance=ps, many=True)
        return serializer.data
        # ps = ps.values_list("phone", flat=True)
        # return list(ps)

    # Overriding get fileds for diff methods
    def get_fields(self):
        fields = super().get_fields()

        # get request object from context
        request = self.context.get('request')
        if request and (request.method.lower() == "post" or request.method.lower() == "put" or request.method.lower() == "patch"):
            # serializer email fields with EmailSerializer
            # fields["email"] = EmailAccountSerializer(request.data)
            fields["emails"] = serializers.ListField()
            fields["phones"] = serializers.ListField()
        # if request and request.method.lower() == "get":
        #     fields["emails"] = EmailAccountSerializer()
        return fields

    def create(self, validated_data):
        contact_instance = Contact.objects.create(first_name=validated_data['first_name'], mid_name=validated_data['mid_name'], last_name=validated_data['last_name'])
        for eml in validated_data['emails']:
            contact_instance.email_set.create(email=eml)
        for phn_d in validated_data['phones']:
            contact_instance.phone_set.create(**phn_d)
        return validated_data

    def update(self, contact_instance, validated_data):
        result = super().update(contact_instance, validated_data)           # updates contact instance

        # validated data has emails or phone fields needed to update
        if "emails" in validated_data:
            contact_instance.email_set.all().delete()
            for eml in validated_data['emails']:
                contact_instance.email_set.create(email=eml)

        if "phones" in validated_data:
            contact_instance.phone_set.all().delete()
            for phn_d in validated_data['phones']:
                contact_instance.phone_set.create(**phn_d)
        return result

    # def validate_emails(self, emails):
    #     raise ValidationError('validation')

class EmailAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailAccount
        fields = ["email"]
        read_only = ("id", )


class PhoneDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneDetail
        fields = ["phone", "label"]
        read_only = ("id", )