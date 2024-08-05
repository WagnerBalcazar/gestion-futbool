from enum import Enum
from typing import List

class SistemaCampeonato(Enum):
    LIGA = "LIGA"
    MUERTE_SUBITA = "MUERTE_SUBITA"
    FASE_GRUPOS = "FASE_GRUPOS"

class Tarjeta(Enum):
    AMARILLA = "AMARILLA"
    ROJA = "ROJA"

class Estado(Enum):
    TITULAR = "TITULAR"
    SUPLENTE = "SUPLENTE"
    EXPULSADO = "EXPULSADO"

class Genero(Enum):
    MASCULINO = "MASCULINO"
    FEMENINO = "FEMENINO"

class PosicionEquipo(Enum):
    ARQUERO = "ARQUERO"
    DEFENSA = "DEFENSA"
    MEDIOCAMPISTA = "MEDIOCAMPISTA"
    DELANTERO = "DELANTERO"

class Estadistica:
    def __init__(self):
        self.nroPenalizaciones = 0
        self.nroTotalGoles = 0
        self.nroTotalRematesArco = 0
        self.nroTotalTiroEsquina = 0
        self.precisionPases = 0
        self.posesionBalon = 0
        self.nroTotalPases = 0

class EstadisticaEquipo(Estadistica):
    def __init__(self):
        super().__init__()
        self.nroPuntosPartido = 0

class EstadisticaIndividual(Estadistica):
    def __init__(self):
        super().__init__()
        self.nroTotalTarjetas = 0

class TablaPosicion:
    def __init__(self):
        self.puntosEquipo = 0
        self.idTabla = ""

    def registrar_punto_equipo(self, puntosTabla: int):
        self.puntosEquipo += puntosTabla

    def sumar_puntos_equipo(self, puntosTabla: int):
        self.puntosEquipo += puntosTabla

class Inscripcion:
    def __init__(self):
        self.costo = 0

    def iniciar_inscripciones(self) -> bool:
        print("Inscripciones iniciadas")
        return True

    def finalizar_inscripciones(self) -> bool:
        print("Inscripciones finalizadas")
        return True

    def realizar_pago_inscripcion(self) -> bool:
        print("Pago de inscripción realizado")
        return True

class Partido:
    def __init__(self):
        self.duracionMinutos = 0
        self.arbitro = ""
        self.numeroArbitros = 0
        self.marcador = ""

    def iniciar_partido(self) -> bool:
        print("Partido iniciado")
        return True

    def pausar_partido(self) -> bool:
        print("Partido pausado")
        return True

    def reanudar_partido(self) -> bool:
        print("Partido reanudado")
        return True

    def finalizar_partido(self) -> bool:
        print("Partido finalizado")
        return True

    def determinar_resultado(self):
        print("Resultado determinado")

class Campeonato:
    def __init__(self):
        self.fecha = 0
        self.numeroFechas = 0
        self.grupos = ""
        self.sistemaCampeonato = None
        self.inscripcionList = []
        self.partidoList = []

    def iniciar_campeonato(self) -> bool:
        print("Campeonato iniciado")
        return True

    def finalizar_campeonato(self) -> bool:
        print("Campeonato finalizado")
        return True

    def sortear_equipos(self):
        print("Equipos sorteados")

class Deporte:
    def __init__(self):
        self.nombre = ""
        self.noParticipantesEquipo = 0
        self.noEquipos = 0
        self.noPartidos = 0
        self.reglamento = ""
        self.grupoList = []

class Grupo:
    def __init__(self):
        self.nombre = ""
        self.noEquipos = 0
        self.equipoList = []

    def asignar_no_partidos_grupo(self):
        print("Asignados partidos a grupo")

class Equipo:
    def __init__(self):
        self.nombre = ""
        self.noJugadores = 0
        self.noPartidosGanados = 0
        self.noPartidosPerdidos = 0
        self.noPartidosEmpatados = 0
        self.noGolesContra = 0
        self.noGolesFavor = 0
        self.puntos = 0
        self.jugadorList = []

class Jugador:
    def __init__(self):
        self.numero = 0
        self.nombre = ""
        self.noTarjetasRecibidas = 0
        self.estado = None
        self.genero = None
        self.posicionEquipo = None

    def anotar_gol(self, noGoles: int) -> bool:
        print(f"{self.nombre} anotó {noGoles} goles")
        return True

class Arbitro:
    def __init__(self):
        self.tarjeta = ""

    def penalizar_jugador(self, tarjeta: str) -> bool:
        print(f"Jugador penalizado con tarjeta {tarjeta}")
        return True

def main():
    # Crear un campeonato
    campeonato = Campeonato()
    campeonato.fecha = int(input("Ingrese el año del campeonato: "))
    campeonato.numeroFechas = int(input("Ingrese el número de fechas del campeonato: "))
    campeonato.grupos = input("Ingrese los grupos del campeonato (separados por comas): ")
    sistema_campeonato = input("Ingrese el sistema de campeonato (LIGA, MUERTE_SUBITA, FASE_GRUPOS): ")
    campeonato.sistemaCampeonato = SistemaCampeonato[sistema_campeonato]

    # Iniciar inscripciones
    inscripcion = Inscripcion()
    inscripcion.iniciar_inscripciones()
    inscripcion.realizar_pago_inscripcion()
    inscripcion.finalizar_inscripciones()

    # Añadir inscripciones al campeonato
    campeonato.inscripcionList.append(inscripcion)

    # Iniciar el campeonato
    campeonato.iniciar_campeonato()

    # Crear equipos y jugadores
    equipo1 = Equipo()
    equipo1.nombre = input("Ingrese el nombre del equipo: ")

    while True:
        jugador = Jugador()
        jugador.nombre = input("Ingrese el nombre del jugador: ")
        jugador.numero = int(input("Ingrese el número del jugador: "))
        estado = input("Ingrese el estado del jugador (TITULAR, SUPLENTE, EXPULSADO): ")
        jugador.estado = Estado[estado]
        genero = input("Ingrese el género del jugador (MASCULINO, FEMENINO): ")
        jugador.genero = Genero[genero]
        posicion = input("Ingrese la posición del jugador (ARQUERO, DEFENSA, MEDIOCAMPISTA, DELANTERO): ")
        jugador.posicionEquipo = PosicionEquipo[posicion]

        equipo1.jugadorList.append(jugador)

        continuar = input("¿Desea añadir otro jugador? (s/n): ")
        if continuar.lower() != 's':
            break

    # Añadir equipos al campeonato
    grupoA = Grupo()
    grupoA.nombre = input("Ingrese el nombre del grupo: ")
    grupoA.equipoList.append(equipo1)

    campeonato.partidoList.append(Partido())

    # Sortear equipos
    campeonato.sortear_equipos()

    # Iniciar y finalizar un partido
    partido = Partido()
    partido.iniciar_partido()
    partido.determinar_resultado()
    partido.finalizar_partido()

    # Finalizar el campeonato
    campeonato.finalizar_campeonato()

if __name__ == "__main__":
    main()
