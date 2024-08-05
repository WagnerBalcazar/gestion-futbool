import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Campeonato {
    private String nombre;
    private String tipo;
    private Date fechaInicio;
    private Date fechaFin;
    private List<EncuentroDeportivo> encuentros = new ArrayList<>();
    private TablaPosicion tablaPosicion = new TablaPosicion();
    private List<Equipo> equipos = new ArrayList<>();

    public void agregarEquipo(Equipo equipo, int puntos) {
        equipos.add(equipo);
        tablaPosicion.agregarEquipo(equipo, puntos);
    }

    public void mostrarTablaPosicion() {
        tablaPosicion.mostrarTabla();
    }

    public void generarEncuentros() {
        // Lógica para generar encuentros (vacío por ahora)
    }

    public void actualizarTablaPosicion() {
        // Lógica para actualizar la tabla de posiciones (vacío por ahora)
    }

    // Getters y Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public Date getFechaInicio() {
        return fechaInicio;
    }

    public void setFechaInicio(Date fechaInicio) {
        this.fechaInicio = fechaInicio;
    }

    public Date getFechaFin() {
        return fechaFin;
    }

    public void setFechaFin(Date fechaFin) {
        this.fechaFin = fechaFin;
    }

    public List<EncuentroDeportivo> getEncuentros() {
        return encuentros;
    }

    public void setEncuentros(List<EncuentroDeportivo> encuentros) {
        this.encuentros = encuentros;
    }

    public List<Equipo> getEquipos() {
        return equipos;
    }

    public void setEquipos(List<Equipo> equipos) {
        this.equipos = equipos;
    }
}
