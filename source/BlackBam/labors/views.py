#coding=utf-8#

from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from BlackBam.labors.models import Department, Labor, Attendance, Salary, SalaryStatement
from BlackBam.labors.serializers import DepartmentSerializer, LaborSerializer, AttendanceSerializer, SalarySerializer, SalaryStatementSerializer


#Regular Views (Department) ************************************************************************


#API Views (Department) ****************************************************************************

class DepartmentList(APIView):
	"""
	List all departments, or create a new department.
	"""
	def get(self, request, format=None):
		departments = Department.objects.all()
		serializer = DepartmentSerializer(departments, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = DepartmentSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetail(APIView):
	"""
	Retrive, update or delete a department instance.
	"""
	def get_object(self, pk):
		try:
			return Department.objects.get(pk=pk)
		except Department.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		department = self.get_object(pk)
		serializer = DepartmentSerializer(labor)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		labor = self.get_object(pk)
		serializer = DepartmentSerializer(labor, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		labor = self.get_object(pk)
		labor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


#Regular Views (Labor) *****************************************************************************


#API Views (Labor) *********************************************************************************
class LaborList(APIView):
    """
    List all labors, or create a new labor.
    """
    def get(self, request, format=None):
        labors = Labor.objects.all()
        serializer = LaborSerializer(labors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LaborSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaborDetail(APIView):
    """
    Retrieve, update or delete a labor instance.
    """
    def get_object(self, pk):
        try:
            return Labor.objects.get(pk=pk)
        except Labor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        labor = self.get_object(pk)
        serializer = LaborSerializer(labor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        labor = self.get_object(pk)
        serializer = LaborSerializer(labor, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        labor = self.get_object(pk)
        labor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Regular Views (Attendance) ************************************************************************


#API Views (Attendance) ****************************************************************************
class AttendanceList(APIView):
    """
    List all attendences, or create a new attendence.
    """
    def get(self, request, format=None):
        attendances = Attendance.objects.all()
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AttendanceSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceDetail(APIView):
    """
    Retrieve, update or delete a attendence instance.
    """
    def get_object(self, pk):
        try:
            return Attendance.objects.get(pk=pk)
        except Attendance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        attendance = self.get_object(pk)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        attendance = self.get_object(pk)
        serializer = AttendanceSerializer(attendance, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        attendance = self.get_object(pk)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Regular Views (Salary) ****************************************************************************


#API Views (Salary) ********************************************************************************
class SalaryList(APIView):
    """
    List all salaries, or create a new salary.
    """
    def get(self, request, format=None):
        salaries = Salary.objects.all()
        serializer = SalarySerializer(salaries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SalarySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalaryDetail(APIView):
    """
    Retrieve, update or delete a salary instance.
    """
    def get_object(self, pk):
        try:
            return Salary.objects.get(pk=pk)
        except Salary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        salary = self.get_object(pk)
        serializer = SalarySerializer(salary)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        salary = self.get_object(pk)
        serializer = SalarySerializer(salary, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        salary = self.get_object(pk)
        salary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Regular Views (SalaryStatement) *********************************************************************


#API Views (SalaryStatement) *************************************************************************
class SalaryStatementList(APIView):
    """
    List all SalaryStaments, or create a new SalaryStament.
    """
    def get(self, request, format=None):
        salaryStatements = SalaryStatement.objects.all()
        serializer = SalaryStatementSerializer(salaryStatements, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SalaryStatementSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalaryStatementDetail(APIView):
    """
    Retrieve, update or delete a SalaryStament instance.
    """
    def get_object(self, pk):
        try:
            return SalaryStatement.objects.get(pk=pk)
        except SalaryStatement.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        salaryStatement = self.get_object(pk)
        serializer = SalaryStatementSerializer(salaryStatement)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        salaryStatement = self.get_object(pk)
        serializer = SalaryStatementSerializer(salaryStatement, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        salaryStatement = self.get_object(pk)
        salaryStatement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)