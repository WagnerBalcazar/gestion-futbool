import java.util.ArrayList;
import java.util.List;

public class TablaPosicion {
    private List<Equipo> equipos = new ArrayList<>();

    public void agregarEquipo(Equipo equipo, int puntos) {
        equipo.getEstadisticas().setPuntos(puntos);
        equipos.add(equipo);
    }

    public void mostrarTabla() {
        System.out.println("Tabla de Posiciones:");
        for (Equipo equipo : equipos) {
            System.out.println("Equipo: " + equipo.getNombre() + " - Puntos: " + equipo.getEstadisticas().getPuntos());
        }
    }
}

