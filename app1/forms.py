from dataclasses import fields
from tkinter import Widget
from django import forms
from app1.models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields="__all__"

        labels={
            'id':'Laptop ID',
            'brand_name':'Brand Name',
            'model_name':'Model Name',
            'price':'PRICE',
            'rom':'ROM',
            'ram':'RAM',
            'SSD':'SSD',
            'HDD':'HDD',
            'weight':'Weight',
            'year':'Year'
            }
        Widgets={
            'id':forms.NumberInput(
                attrs={
                    'placeholder':'eg.HP-112212'
                }
            ),
            'brand_name':forms.TextInput(
                attrs={
                    'placeholder':'eg.HP'
                }
            ),
            'model_name':forms.TextInput(
                attrs={
                    'placeholder':'HP-15s-fg256567TV'
                }
            )
        }