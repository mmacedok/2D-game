extends CharacterBody2D

const SPEED := 76.0

@onready var sprite: Sprite2D = $Sprite2D

func _physics_process(_delta: float) -> void:
	var direction := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	var wasd := Vector2(
		int(Input.is_physical_key_pressed(KEY_D)) - int(Input.is_physical_key_pressed(KEY_A)),
		int(Input.is_physical_key_pressed(KEY_S)) - int(Input.is_physical_key_pressed(KEY_W))
	)
	if wasd != Vector2.ZERO:
		direction = wasd.normalized()
	if direction.x != 0.0:
		sprite.flip_h = direction.x < 0.0
	velocity = direction * SPEED
	move_and_slide()
