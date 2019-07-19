import json
import logging

from actions import resolve
from protocol import (
    validate_request, make_response, make_404, make_400
)

logger = logging.getLogger('server.main')


def default_handler(raw_request):

    request = json.loads(raw_request)
    action_name = request.get('action')

    if validate_request(request):
        controller = resolve(action_name)
        if controller:
            try:
                response = controller(request)
            except Exception as err:
                logger.critical(err)
                response = make_response(request, 500, 'Internal server error')
        else:
            logger.error(f'Action with name {action_name} does not exists')
            response = make_404(request)
    else:
        logger.error('request is not valid')
        response = make_400(request)

    return json.dumps(response)
