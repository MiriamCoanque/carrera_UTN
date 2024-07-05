import pygame
from datos import lista
from constantes import *
import json

lista_pregunta = []
lista_opcion_a = []
lista_opcion_b = []
lista_opcion_c = []
lista_tema = []
lista_respuesta_correcta = []
indice = 0
acumulador_puntaje = 0

for e_lista in lista:
    lista_pregunta.append(e_lista["pregunta"])
    lista_opcion_a.append(e_lista["a"])
    lista_opcion_b.append(e_lista["b"])
    lista_opcion_c.append(e_lista["c"])
    lista_tema.append(e_lista["tema"])
    lista_respuesta_correcta.append(e_lista["correcta"])

pygame.init()

#---------------------VENTANA----------------------------------------------
ANCHO_VENTANA = 1300
ALTO_VENTANA = 800
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Carrera UTN")  # NOMBRE DEL JUEGO

#---------------------CUADRADOS----------------------------------------------
rect_comenzar = pygame.Rect(250, 650, 200, 100)  # BOTON COMENZAR
rect_terminar = pygame.Rect(500, 650, 200, 100)  # BOTON DE TERMINAR
rect_opcion_a = pygame.Rect(300, 190, 100, 50)
rect_opcion_b = pygame.Rect(500, 190, 100, 50)
rect_opcion_c = pygame.Rect(700, 190, 100, 50)
rect_contenido = pygame.Rect(270, 40, 690, 190)

rect_casilla1 = pygame.Rect(270, 400, 100, 50)
rect_casilla2 = pygame.Rect(380, 400, 100, 50)
rect_casilla3 = pygame.Rect(490, 400, 100, 50)
rect_casilla4 = pygame.Rect(600, 400, 100, 50)
rect_casilla5 = pygame.Rect(710, 400, 100, 50)
rect_casilla6 = pygame.Rect(820, 400, 100, 50)
rect_casilla7 = pygame.Rect(930, 400, 100, 50)
rect_casilla8 = pygame.Rect(1040, 400, 100, 50)

rect_casilla9 = pygame.Rect(270, 530, 100, 50)
rect_casilla10 = pygame.Rect(380, 530, 100, 50)
rect_casilla11 = pygame.Rect(490, 530, 100, 50)
rect_casilla12 = pygame.Rect(600, 530, 100, 50)
rect_casilla13 = pygame.Rect(710, 530, 100, 50)
rect_casilla14 = pygame.Rect(820, 530, 100, 50)
rect_casilla15 = pygame.Rect(930, 530, 100, 50)
rect_casilla16 = pygame.Rect(1040, 530, 100, 50)

#--------------------FUENTES Y TEXTOS--------------------------------------
fuente = pygame.font.SysFont("Arial Black", 19)
fuente_pequeño = pygame.font.SysFont("ArialBlack ", 18)
fuente_grande = pygame.font.SysFont("Arial Black", 25)

texto_comenzar = fuente_grande.render("COMENZAR", True, COLOR_AMARILLO)
texto_terminar = fuente_grande.render("TERMINAR", True, COLOR_AMARILLO)
texto_puntaje = fuente_grande.render("PUNTAJE", True, COLOR_AMARILLO)
texto_tiempo = fuente_grande.render("Tiempo:", True, COLOR_AMARILLO)
texto_inicio = fuente.render("SALIDA", True, COLOR_ROJO)
texto_llegada = fuente.render("LLEGADA", True, COLOR_ROJO)
texto_avanza_uno = fuente_pequeño.render("Avanza 1", True, COLOR_AMARILLO)
texto_retrocede_uno = fuente_pequeño.render("Retrocede 1", True, COLOR_AMARILLO)


#-------------------BANDERAS-----------------------------------------------
mostrar_preguntas = False
flag_correr = True
terminar = False
fin_tiempo = False
empezar = True

#-------------------TEMPORIZADOR-------------------------------------------
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000)  # 1000 ES UN SEGUNDO
segundos = 5

#-----------------IMAGENES-------------------------------------------------
imagen_logo = pygame.image.load("logotipo.png")
imagen_logo = pygame.transform.scale(imagen_logo, (250, 250))
posicion_logo = [10, 10]

imagen_estudiante = pygame.image.load("estudiante.png")
imagen_estudiante = pygame.transform.scale(imagen_estudiante, (100, 110))
posicion_estudiante = [100, 300]

imagen_flecha_inicio = pygame.image.load("flecha-derecha.png")
imagen_flecha_inicio = pygame.transform.scale(imagen_flecha_inicio, (110, 120))
posicion_flecha_inicio = [120, 360]

imagen_flecha_girar = pygame.image.load("deshacer2.png")
imagen_flecha_girar = pygame.transform.scale(imagen_flecha_girar, (150, 160))
posicion_flecha_girar = [1140, 420]

imagen_utn = pygame.image.load("utn.jpg")
imagen_utn = pygame.transform.scale(imagen_utn, (130, 90))
posicion_utn = [120, 500]

#-------------------ENTRADA DE TEXTO---------------------------------------
ingreso = ""
ingreso_rect = pygame.Rect(500, 200, 200, 40)

while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)

            # CLICK AL BOTON DE COMENZAR
            if rect_comenzar.collidepoint(posicion_click):
                terminar = False
                fin_tiempo = False
                empezar = True
                mostrar_preguntas = True
                acumulador_puntaje = 0
                indice = 0
                segundos = 5
                ingreso = ""

            # CLICK AL BOTON TERMINAR
            if rect_terminar.collidepoint(posicion_click):
                empezar = False
                terminar = True
                mostrar_preguntas = False
                segundos = "Fin del juego"

                try:

                    with open("puntajes.json", "r") as archivo:
                        puntajes = json.load(archivo)
                except FileNotFoundError:
                    puntajes = []


                puntajes.append({"nombre": ingreso, "puntaje": acumulador_puntaje})
                puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)[:10]

                with open("puntajes.json", "w") as archivo:
                    json.dump(puntajes, archivo, indent=4)

            
            if mostrar_preguntas:
                respuesta_seleccionada = None
                if rect_opcion_a.collidepoint(posicion_click):
                    respuesta_seleccionada = "a"
                elif rect_opcion_b.collidepoint(posicion_click):
                    respuesta_seleccionada = "b"
                elif rect_opcion_c.collidepoint(posicion_click):
                    respuesta_seleccionada = "c"
                
                if respuesta_seleccionada:
                    if respuesta_seleccionada == lista_respuesta_correcta[indice]:
                        acumulador_puntaje += 10
                    
                    indice += 1
                    if indice >= len(lista_pregunta):
                        mostrar_preguntas = False
                        fin_tiempo = True
                    else:
                        segundos = 5  # REINICIAR TEMPORIZADOR

        if evento.type == timer_segundos:
            if mostrar_preguntas and not fin_tiempo:
                segundos -= 1
                if segundos == 0:
                    indice += 1
                    if indice >= len(lista_pregunta):
                        mostrar_preguntas = False
                        fin_tiempo = True
                        segundos = "Se terminó el tiempo"
                    else:
                        segundos = 5  # REINICIAR TEMPORIZADOR

        if evento.type == pygame.KEYDOWN and terminar:
            if evento.key == pygame.K_BACKSPACE:
                ingreso = ingreso[:-1]
            else:
                ingreso += evento.unicode

    pantalla.fill(GRAY7)

    if empezar:
        pygame.draw.rect(pantalla, GRAY48, rect_contenido)
        segundos_texto = fuente_grande.render(str(segundos), True, COLOR_AMARILLO)
        pantalla.blit(segundos_texto, (1120, 50))
        puntaje_texto = fuente_grande.render(f"Puntaje: {str(acumulador_puntaje)}", True, COLOR_AMARILLO)
        pantalla.blit(puntaje_texto, (1000, 100))

        pantalla.blit(imagen_flecha_inicio, (posicion_flecha_inicio))
        pantalla.blit(imagen_flecha_girar, (posicion_flecha_girar))
        pantalla.blit(imagen_estudiante, (posicion_estudiante))
        pantalla.blit(imagen_utn, (posicion_utn))
        pantalla.blit(texto_tiempo, (1000, 50))
        pantalla.blit(texto_inicio, (133, 405))
        pantalla.blit(texto_llegada, (133, 600))  # x y
        
        pygame.draw.rect(pantalla, GRAY48, rect_casilla1)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla2)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla3)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla4)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla5)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla6)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla7)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla8)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla9)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla10)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla11)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla12)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla13)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla14)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla15)
        pygame.draw.rect(pantalla, GRAY48, rect_casilla16)
        pantalla.blit(texto_avanza_uno, (rect_casilla6))
        pantalla.blit(texto_retrocede_uno, (rect_casilla12))

    if mostrar_preguntas:
        pregunta_actual = lista_pregunta[indice]
        tema_titulo = lista_tema[indice]
        opcion_a = lista_opcion_a[indice]
        opcion_b = lista_opcion_b[indice]
        opcion_c = lista_opcion_c[indice]

        preguntas_del_juego = fuente.render(pregunta_actual, True, COLOR_BLANCO)
        texto_tema_titulo = fuente_pequeño.render(f"Categoria {tema_titulo}", True, COLOR_AMARILLO)
        texto_opcion_a = fuente_pequeño.render(opcion_a, True, COLOR_AMARILLO)
        texto_opcion_b = fuente_pequeño.render(opcion_b, True, COLOR_AMARILLO)
        texto_opcion_c = fuente_pequeño.render(opcion_c, True, COLOR_AMARILLO)

        pantalla.blit(preguntas_del_juego, (290, 50))
        pantalla.blit(texto_tema_titulo, (300, 100))
        pantalla.blit(texto_opcion_a, (rect_opcion_a.x, rect_opcion_a.y))
        pantalla.blit(texto_opcion_b, (rect_opcion_b.x, rect_opcion_b.y))
        pantalla.blit(texto_opcion_c, (rect_opcion_c.x, rect_opcion_c.y))

    if terminar:
        pygame.draw.rect(pantalla, COLOR_BLANCO, ingreso_rect, 2)
        texto_superficie = fuente.render(ingreso, True, COLOR_BLANCO)
        pantalla.blit(texto_superficie, (ingreso_rect.x + 5, ingreso_rect.y + 5))
        pantalla.blit(texto_puntaje, (500, 100))
        puntaje_texto = fuente.render(str(acumulador_puntaje), True, COLOR_AMARILLO)
        pantalla.blit(puntaje_texto, (650, 100))  #PUNTAJE FINAL

    pygame.draw.rect(pantalla, GRAY48, rect_comenzar)
    pygame.draw.rect(pantalla, GRAY48, rect_terminar)
    pantalla.blit(imagen_logo, (posicion_logo))
    pantalla.blit(texto_comenzar, (270, 690))
    pantalla.blit(texto_terminar, (520, 690))



    # MOSTRAR CAMBIOS EN PANTALLA
    pygame.display.flip()

pygame.quit()
