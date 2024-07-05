from django import forms


# 继承bootstrap样式
class BootStrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = field.label
                field.widget.attrs['step'] = 0.01
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label,
                    'step': 0.01
                }


class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


class BootstrapForm(BootStrap, forms.Form):
    pass
