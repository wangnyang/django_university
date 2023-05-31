from django.forms import ModelForm
from .models import Mark, Lesson, Student


class AddMarkForm(ModelForm):
    def __init__(self, lesson: Lesson, **kwargs):
        super(AddMarkForm, self).__init__(**kwargs)
        self.fields['student'].queryset = Student.objects.filter(group__in=lesson.groups.all())
        self.fields['lesson'].queryset = Lesson.objects.filter(id=lesson.id)

    class Meta:
        model = Mark
        fields = ['mark', 'presence', 'student', 'lesson']

    # def clean_title(self):
    #     title = self.cleaned_data["title"]
    #     if not title:
    #         return title

    #     if not title[0].isupper():
    #         self.add_error("title", "Should start with an uppercase letter")

    #     if title.endswith("."):
    #         self.add_error("title", "Should not end with a full stop")

    #     if "&" in title:
    #         self.add_error("title", "Use 'and' instead of '&'")

    #     return title


# у формы проблема она нихрена не сохраняет и никто не знает почему
