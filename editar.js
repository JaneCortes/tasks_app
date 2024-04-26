<script>
    // Esta función permite editar una tarea existente.
    function editarTarea(id, tarea) {
        // Se muestra un cuadro de diálogo al usuario con un campo de entrada para editar la tarea.
        var nuevaTarea = prompt("Editar Tarea", tarea);
        
        // Si el usuario ingresó un valor (es decir, no presionó 'Cancelar' en el cuadro de diálogo),
        // entonces actualizamos el valor de la tarea y enviamos el formulario.
        if (nuevaTarea != null) {
            // Actualizamos el valor de la tarea en el formulario.
            document.getElementById('tarea' + id).value = nuevaTarea;
            
            // Enviamos el formulario.
            document.getElementById('form' + id).submit();
        }
    }
</script>
