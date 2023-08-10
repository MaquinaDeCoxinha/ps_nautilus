import rospy
import tf2_ros
import yaml
import math
from geometry_msgs.msg import TransformStamped

def load_parameters():
    # Carregue os parâmetros do arquivo YAML
    with open(rospy.get_param("sistema_solar_params_path"), 'r') as file:
        return yaml.safe_load(file)

def broadcast_transforms():
    params = load_parameters()

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    tf_broadcaster = tf2_ros.TransformBroadcaster()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        try:
            for planeta in params['planetas']:
                # Calcule a posição angular do planeta com base no tempo
                angular_position = 2.0 * math.pi * current_time.to_sec() / planeta['periodo_orbita']

                # Calcule as coordenadas x e y com base no raio da órbita e na posição angular
                x = planeta['raio_orbita'] * math.cos(angular_position)
                y = planeta['raio_orbita'] * math.sin(angular_position)

                # Crie a mensagem de transformação
                transform = TransformStamped()
                transform.header.stamp = current_time
                transform.header.frame_id = params['estrela']
                transform.child_frame_id = planeta['nome']
                transform.transform.translation.x = x
                transform.transform.translation.y = y
                transform.transform.rotation.w = 1.0

                # Envie a transformação
                tf_broadcaster.sendTransform(transform)

                # Transformações dos satélites (se houver)
                for satelite in planeta.get('satelites', []):
                    # Calcule a posição angular do satélite em relação ao planeta
                    angular_position_sat = 2.0 * math.pi * current_time.to_sec() / satelite['periodo_orbita']

                    # Calcule as coordenadas x e y do satélite com base no raio da órbita e na posição angular
                    x_sat = satelite['raio_orbita'] * math.cos(angular_position_sat)
                    y_sat = satelite['raio_orbita'] * math.sin(angular_position_sat)

                    # Crie a mensagem de transformação para o satélite em relação ao planeta
                    transform_sat = TransformStamped()
                    transform_sat.header.stamp = current_time
                    transform_sat.header.frame_id = planeta['nome']
                    transform_sat.child_frame_id = satelite['nome']
                    transform_sat.transform.translation.x = x_sat
                    transform_sat.transform.translation.y = y_sat
                    transform_sat.transform.rotation.w = 1.0

                    # Envie a transformação do satélite
                    tf_broadcaster.sendTransform(transform_sat)
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            pass

        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('sistema_solar')

    # Carregue os parâmetros
    params_path = rospy.get_param("~params_path", "config/sistema_solar_params.yaml")
    rospy.set_param("sistema_solar_params_path", params_path)

    broadcast_transforms()
