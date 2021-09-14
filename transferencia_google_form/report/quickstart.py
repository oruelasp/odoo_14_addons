from tempfile import gettempdir
import io
import logging
from .Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

tmp = gettempdir()

CLIENT_SECRET_FILE = '/mnt/extra-addons/transferencia_google_form/report/client_secret_file_2.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
_logger = logging.getLogger(__name__)


def download_files(file_ids, file_names, SKIP_TOKEN):
    service = Create_Service(SKIP_TOKEN, CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    for file_id, file_name in zip(file_ids, file_names):
        request = service.files().get_media(fileId=file_id)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        done = False

        while not done:
            status, done = downloader.next_chunk()
            print('Donwload progress {0}'.format(status.progress() * 100))

        fh.seek(0)

        with open('{}/{}'.format(tmp, file_name), 'wb') as f:
            try:
                f.write(fh.read())
            except Exception as e:
                _logger.error(u'Excepción al crear archivo temporal: {}'.format(e))
            f.close()

# download_files(['1G0ApL0c5XVTjSLln0dy99D6ZsZ14Qeg3', '1nCW767VPiY722RNJ6W5XG_XT3LY2cPWW', '1UauGcVDArur8sOKCsm_RIYqaXgZII4hl'], ['image1.jpg', 'image2.jpg', 'image3.jpg'])