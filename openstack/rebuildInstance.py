import openstack
import sys

# Initialize and turn on debug logging
openstack.enable_logging(debug=False)


def create_connection(auth_url, domain, project_name, username, password):

    return openstack.connect(
        auth_url=auth_url,
        project_name=project_name,
        username=username,
        password=password,
        domain_name=domain,
        app_name='python3',
        app_version='1.0',
    )


def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        print(server)


def list_images(conn):
    print("List Images:")

    for image in conn.image.images():
        print(image)


conn = create_connection(auth_url='http://10.206.5.12:5000/v3/', domain='Default',
                         project_name='vdp', username='jenkins', password='jenkins')


def rebuildInstance(conn, serverId, imageId):
    #imageId = conn.get_server(serverId).image['id']
    conn.rebuild_server(serverId, imageId)

if len(sys.argv) != 3:
    print('[INSTANCE_ID] [IMAGE_ID]')
    exit(1)

rebuildInstance(conn, sys.argv[1], sys.argv[2])
