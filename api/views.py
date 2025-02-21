from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re
import logging

logger = logging.getLogger('api')

class JsonView(APIView):
    def post(self, request):
        try:
            logger.debug(f"Received request data: {request.data}")
            data = request.data.get("data", [])
            if not isinstance(data, list):
                logger.error("Invalid input: data must be an array")
                return Response({"error": "Invalid input: data must be an array"}, status=status.HTTP_400_BAD_REQUEST)

            numbers = []
            alphabets = []
            highest_alphabet = []

            for item in data:
                if isinstance(item, str):
                    if re.match(r"^\d+$", item):
                        numbers.append(item)
                    elif re.match(r"^[A-Za-z]$", item):
                        alphabets.append(item)
                else:
                    logger.warning(f"Skipping invalid item: {item}")

            if alphabets:
                highest_alphabet = [max(alphabets, key=str.lower)]
                logger.debug(f"Highest alphabet determined: {highest_alphabet}")

            response_data = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet,
            }
            logger.info(f"Returning response: {response_data}")
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.exception(f"Error processing request: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)