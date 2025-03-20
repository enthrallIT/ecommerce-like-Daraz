from django import forms
from .models import Product, Category, Offer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount_price', 'discount_percent', 'image', 'category', 'buying_price', 'quantity', 'rent_cost', 'worker_cost', 'other_cost', 'profit']

    def clean(self):
        cleaned_data = super().clean()
        discount_percent = cleaned_data.get('discount_percent')
        discount_price = cleaned_data.get('discount_price')

        if discount_percent and discount_price:
            raise forms.ValidationError("Please select one")
        
        return cleaned_data
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image', 'is_show']
class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['title', 'image', 'is_active']
