from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from theory.models import Course
from .models import Question, Answer, Test 
from theory.serializers import CourseSerializer
from .serializers import QuestionSerializer, AnswerSerializer, TestSerializer


class TestsListView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


    def get(self, request):
        courses = Course.objects.all()
        result_data = []

        for course in courses:
            course_title = course.title
            tests = Test.objects.filter(course=course)
            tests_list = []

            for test in tests:
                test_title = test.title
                questions = Question.objects.filter(test=test)
                questions_list = []

                for question in questions:
                    question_serializer = QuestionSerializer(question)
                    answers = question.answers.all()  # Фильтруем только правильные ответы
                    answer_serializer = AnswerSerializer(answers, many=True)

                    questions_list.append({
                        'question_text': question_serializer.data['text'],
                        'answers': answer_serializer.data,
                    })

                tests_list.append({
                    'test_title': test_title,
                    'questions': questions_list
                })

            result_data.append({
                'course_title': course_title,
                'tests': tests_list
            })

        return Response(result_data, status=status.HTTP_200_OK)
