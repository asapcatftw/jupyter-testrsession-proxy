import os
import tempfile
import subprocess
import getpass
import shutil
from textwrap import dedent

def setup_testshiny():
    '''Manage a TestShiny instance.'''

    name = 'testshiny'
    def _get_testshiny_cmd(port):
        conf = dedent("""
            run_as {user};
            server {{
                listen {port};
                location / {{
                    site_dir {site_dir};
                    log_dir {site_dir}/logs;
                    directory_index on;
                }}
            }}
        """).format(
            user=getpass.getuser(),
            port=str(port),
            site_dir=os.getcwd()
        )

        f = tempfile.NamedTemporaryFile(mode='w', delete=False)
        f.write(conf)
        f.close()
        return ['shiny-server', f.name]

    return {
        'command': _get_testshiny_cmd,
        'launcher_entry': {
            'title': 'TestShiny',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'shiny.svg')
        }
    }

