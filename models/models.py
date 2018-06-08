# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Instituto(models.Model):
    _name = 'educacion.instituto'

    name = fields.Char(string="Nombre del Instituto")
    foto_instituto = fields.Binary(string="Imagen del Instituto")
    fecha_de_apertura = fields.Date(string="Apertura")
    direccion = fields.Char(string="Dirección del Instituto")
    email = fields.Char(string="Dirección email del Instituto", default="@gmail.com")
    telefono = fields.Char(string="Teléfono del Instituto", size=9)
    pais_id = fields.Many2one('res.country', string="País")
    departamento_id = fields.Many2one('educacion.departamento', string="Departamentos")

class Departamento(models.Model):
    _name = 'educacion.departamento'

    name = fields.Char(string="Nombre de Departamento")
    rama_del_departamento = fields.Char(string="Rama del Departamento")
    num_profesores = fields.Integer(string="Número de Profesores")
    jefe_de_departamento = fields.Many2one('educacion.profesor', string="Jefe de Departamento")
    institutos = fields.One2many('educacion.instituto', 'departamento_id', string="Institutos")

class Alumno(models.Model):
    _name = 'educacion.alumno'

    name = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    foto_alumno = fields.Binary(string="Foto del Alumno")
    fecha_de_nacimiento = fields.Date(string="Fecha de nacimiento")
    telefono = fields.Char(string="Número de teléfono", size=12)
    dni = fields.Char(string="DNI", size=9)
    email = fields.Char(string="Email", default="@gmail.com")
    sexo = fields.Selection([('hombre','Hombre'),('mujer','Mujer'),('otro','Otro')], default="Género")
    pais_id = fields.Many2one('res.country', string="País")
    curso_id = fields.Many2one('educacion.curso', string="Curso")
    insti = fields.Many2one('educacion.instituto', string="Instituto")


 #<!-- Actividad ampliacion Eduardo -->
class Calen(models.Model):
    _name = 'educacion.calendar'

    name = fields.Char(string="Resumen del evento")
    empiezaen = fields.Datetime(string="Empieza el")
    asignatura = fields.Selection([('redes','Redes'),('gtb','GTB'),('lnd','LND')])
    descrip = fields.Text(string="Descripción")



class Curso(models.Model):
    _name = 'educacion.curso'

    name = fields.Char(string="Nombre")
    num_horas = fields.Integer(string="Número de horas")
    tutor = fields.Char(string="Tutor del curso")
    alumnos = fields.One2many('educacion.alumno', 'curso_id', string="Alumnos")

class Profesor(models.Model):
    _name = 'educacion.profesor'

    name = fields.Char(string="Nombre")
    dni = fields.Char(string="DNI", size=9)
    salario = fields.Integer(string="Salario")
    foto_profesor = fields.Binary(string="Foto del profesor")
    fecha_de_nacimiento = fields.Date(string="Fecha de nacimiento")
    pais_id = fields.Many2one('res.country', string="País")
    notas_id = fields.Many2one('educacion.nota', string="Asignatura")
    curso_id = fields.Many2one('educacion.curso', string="Curso")

class Nota(models.Model):
    _name = 'educacion.nota'

    name = fields.Many2one('educacion.curso', string="Nombre de la asignatura")
    namealu = fields.Many2one('educacion.alumno', string="Nombre del alumno")
    relacion = fields.One2many('educacion.profesor', 'notas_id')
    profesores = fields.Many2one('educacion.profesor', string="Nombre del Profesor")
    nota = fields.Integer(string="Nota")
