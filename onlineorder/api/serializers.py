from rest_framework import serializers
from onlineorder.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_date','purchaser','po_ref_no','project_name','project_site_address','contact_person_and_no','unloading_method','joe_panel_product_code','length','qty','uom','expected_delivery','remarks','status')

    def create(self,validated_data):
        my_incoming_data = validated_data
        inserted_data = Order.objects.create(**validated_data)
        return Response(inserted_data)