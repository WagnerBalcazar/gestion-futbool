import java.util.Date;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Crear un campeonato
        Campeonato campeonato = new Campeonato();
        System.out.println("Ingrese el nombre del campeonato:");
        campeonato.setNombre(scanner.nextLine());
        System.out.println("Ingrese el tipo de campeonato:");
        campeonato.setTipo(scanner.nextLine());
        campeonato.setFechaInicio(new Date());
        campeonato.setFechaFin(new Date());

        // Ingresar número de equipos
        System.out.println("Ingrese el número de equipos:");
        int numEquipos = scanner.nextInt();
        scanner.nextLine(); // Consumir la nueva línea

        // Crear equipos y jugadores
        for (int i = 0; i < numEquipos; i++) {
            // Crear un equipo
            Equipo equipo = new Equipo();
            System.out.println("Ingrese el nombre del equipo " + (i + 1) + ":");
            equipo.setNombre(scanner.nextLine());
            System.out.println("Ingrese el uniforme del equipo " + (i + 1) + ":");
            equipo.setUniforme(scanner.nextLine());

            // Crear jugadores para el equipo
            System.out.println("Ingrese el número de jugadores para el equipo " + equipo.getNombre() + ":");
            int numJugadores = scanner.nextInt();
            scanner.nextLine(); // Consumir la nueva línea
            for (int j = 0; j < numJugadores; j++) {
                Jugador jugador = new Jugador();
                System.out.println("Ingrese el nombre del jugador " + (j + 1) + ":");
                jugador.setNombre(scanner.nextLine());
                System.out.println("Ingrese el apellido del jugador " + (j + 1) + ":");
                jugador.setApellido(scanner.nextLine());
                System.out.println("Ingrese la edad del jugador " + (j + 1) + ":");
                jugador.setEdad(scanner.nextInt());
                scanner.nextLine(); // Consumir la nueva línea
                System.out.println("Ingrese la posición del jugador " + (j + 1) + ":");
                jugador.setPosicion(scanner.nextLine());

                // Inscribir el jugador en el equipo
                equipo.inscribirJugador(jugador);
            }

            // Agregar el equipo al campeonato con puntos iniciales
            System.out.println("Ingrese los puntos iniciales para el equipo " + equipo.getNombre() + ":");
            int puntos = scanner.nextInt();
            scanner.nextLine(); // Consumir la nueva línea
            campeonato.agregarEquipo(equipo, puntos);
        }

        // Mostrar la tabla de posiciones
        campeonato.mostrarTablaPosicion();

        // Registrar un encuentro deportivo (solo ejemplo)
        if (campeonato.getEquipos().size() > 1) {
            EncuentroDeportivo encuentro = new EncuentroDeportivo();
            encuentro.setFecha(new Date());
            encuentro.setEquipoLocal(campeonato.getEquipos().get(0));
            encuentro.setEquipoVisitante(campeonato.getEquipos().get(1));
            encuentro.registrarResultado(); // Necesita implementación
        }

        // Generar encuentros y actualizar tabla de posiciones
        campeonato.generarEncuentros(); // Necesita implementación
        campeonato.actualizarTablaPosicion(); // Necesita implementación

        scanner.close();
    }
}
