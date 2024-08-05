import java.util.ArrayList;
import java.util.List;

public class Equipo {
    private String nombre;
    private String uniforme;
    private List<Jugador> jugadores = new ArrayList<>();
    private EstadisticaEquipo estadisticas = new EstadisticaEquipo();

    public void inscribirJugador(Jugador jugador) {
        jugadores.add(jugador);
    }

    public EstadisticaEquipo getEstadisticas() {
        return estadisticas;
    }

    public void setEstadisticas(EstadisticaEquipo estadisticas) {
        this.estadisticas = estadisticas;
    }

    // Getters y Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getUniforme() {
        return uniforme;
    }

    public void setUniforme(String uniforme) {
        this.uniforme = uniforme;
    }

    public List<Jugador> getJugadores() {
        return jugadores;
    }

    public void setJugadores(List<Jugador> jugadores) {
        this.jugadores = jugadores;
    }
}
