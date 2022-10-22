from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import notesSerializer, Notes


@api_view(['GET'])
def notes(request):
    note = Notes.objects.all()
    serializer = notesSerializer(note, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createnotes(request):
    serializer = notesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def readnotes(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = notesSerializer(instance=note, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def updatenotes(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = notesSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def deletenotes(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response("Deleted Successfully")
