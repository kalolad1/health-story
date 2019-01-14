# For HealthEncounter model.
# Type of health encounter.
SURGERY = 'surgery'
ROUTINE_PHYSICAL = 'routine physical'
GENERAL_ILLNESS = 'general illness'
EMERGENCY_ROOM = 'emergency room'

TYPE_OF_HEALTH_ENCOUNTER = (
    (SURGERY, 'Surgery'),
    (ROUTINE_PHYSICAL, 'Routine Physical'),
    (GENERAL_ILLNESS, 'General Illness'),
    (EMERGENCY_ROOM, 'Emergency Room'),
)

# Dictionary of health encounter types mapped to their Font Awesome icons (used in the
# timeline of the patient story).
HE_TO_ICON = {
    SURGERY: 'fa fa-bed',
    ROUTINE_PHYSICAL: 'fa fa-calendar-check-o',
    GENERAL_ILLNESS: '	fa fa-thermometer-4',
    EMERGENCY_ROOM: 'fa fa-flash',
}