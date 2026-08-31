# {{GAME_TITLE}} — UX, Controls, and Onboarding

## Input model

| Action | Context | Default inputs | Remappable | Hold/toggle/timing | Conflicts and priority |
|---|---|---|---|---|---|
| {{ACTION}} | {{CONTEXT}} | {{INPUTS}} | Yes | {{BEHAVIOR}} | {{RULES}} |

## Screen and state flow

| From | Player action or event | To | Loading/save behavior | Back/error behavior |
|---|---|---|---|---|
| {{SCREEN_OR_STATE}} | {{TRIGGER}} | {{SCREEN_OR_STATE}} | {{BEHAVIOR}} | {{RECOVERY}} |

## HUD and feedback

| Information | Player decision supported | Presentation | Priority | Alternate cue | Edge state |
|---|---|---|---|---|---|
| {{INFORMATION}} | {{DECISION}} | {{VISUAL_AUDIO_HAPTIC}} | {{PRIORITY}} | {{NON_COLOR_OR_NON_AUDIO_CUE}} | {{EMPTY_FULL_ERROR_HIDDEN}} |

## Onboarding sequence

| Step | Required knowledge | Setup | Player action | Feedback | Mastery evidence | Skip/retry behavior |
|---|---|---|---|---|---|---|
| 1 | {{CONCEPT}} | {{SAFE_CONTEXT}} | {{ACTION}} | {{RESPONSE}} | {{OBSERVED_BEHAVIOR}} | {{RULE}} |

## Failure, recovery, and return

- Invalid input: {{FEEDBACK_AND_RECOVERY}}
- Player failure: {{RETRY_CHECKPOINT_AND_LOSS_RULES}}
- Interrupted session: {{PAUSE_SAVE_RESUME_RULES}}
- Returning player: {{REORIENTATION_AND_CHANGED_STATE}}
- Network or platform failure: {{DEGRADED_OR_RECOVERY_FLOW_IF_RELEVANT}}

## Accessibility and settings

| Need | Default | Options | Applies to | Acceptance evidence |
|---|---|---|---|---|
| {{INPUT_PERCEPTION_TIMING_COGNITION_OR_MOTION_NEED}} | {{DEFAULT}} | {{ALTERNATIVES}} | {{SCREENS_OR_SYSTEMS}} | {{TEST}} |

## UX acceptance criteria

- {{FIRST_TIME_DISCOVERY_AND_COMPLETION_TEST}}
- {{CONTROLLER_KEYBOARD_TOUCH_OR_PLATFORM_NAVIGATION_TEST}}
- {{ERROR_RECOVERY_TEST}}
- {{ACCESSIBILITY_OPTION_TEST}}
