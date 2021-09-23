from rest_framework import viewsets
from .serilaizers import ContactSerializer
from contact.models import Contact, EmailAccount, PhoneDetail
from rest_framework import status
from rest_framework.response import Response

class ContactModelViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        EmailAccount.objects.filter(contact_id=instance.id).delete()            # delete emails
        PhoneDetail.objects.filter(contact_id=instance.id).delete()             # delete phones
        instance.delete()           # delete contact
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        contact_instance = self.get_object()
        contact_serializer = self.get_serializer(contact_instance, data=request.data, partial=partial)
        contact_serializer.is_valid(raise_exception=True)
        self.perform_update(contact_serializer)


        return Response(contact_serializer.data)