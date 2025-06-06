# Active Window Widget Options

| Option              | Type    | Default                                                                 | Description                                                                 |
|---------------------|---------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `label`             | string  | `"{win[title]}"`                                                        | The label format for the active window.                                     |
| `label_alt`         | string  | `"[class_name='{win[class_name]}' exe='{win[process][name]}' hwnd={win[hwnd]}]"` | The alternative label format for the active window.                        |
| `label_no_window`   | string  | `None`                                                                  | The label to display when no window is active.                              |
| `label_icon`        | boolean | `True`                                                                  | Whether to display an icon with the label.                                  |
| `label_icon_size`   | integer | `16`                                                                    | The size of the icon displayed with the label.                              |
| `max_length`        | integer | `None`                                                                  | The maximum length of the label text.                                       |
| `max_length_ellipsis` | string | `"..."`                                                                | The ellipsis to use when the label text exceeds the maximum length.         |
| `monitor_exclusive` | boolean | `True`                                                                  | Whether the widget should be exclusive to the monitor.                      |
| `ignore_window`    | dict    | `{'classes': [], 'processes': [], 'titles': []}`                        | Windows to ignore based on class names, process names, and titles.          |
| `callbacks`         | dict    | `{'on_left': 'toggle_label', 'on_middle': 'do_nothing', 'on_right': 'do_nothing'}` | Callbacks for mouse events on the widget.                        |
| `container_padding`  | dict | `{'top': 0, 'left': 0, 'bottom': 0, 'right': 0}`      | Explicitly set padding inside widget container. |
| `animation`         | dict    | `{'enabled': True, 'type': 'fadeInOut', 'duration': 200}`               | Animation settings for the widget.                                          |
| `container_shadow`   | dict   | `None`                  | Container shadow options.                       |
| `label_shadow`         | dict   | `None`                  | Label shadow options.                 |

## Example Configuration

```yaml
active_window:
  type: "yasb.active_window.ActiveWindowWidget"
  options:
    label: "{win[title]}"
    label_alt: "[class_name='{win[class_name]}' exe='{win[process][name]}' hwnd={win[hwnd]}]"
    label_no_window: ""
    label_icon: true
    label_icon_size: 16
    max_length: 56
    max_length_ellipsis: "..."
    monitor_exclusive: true
    label_shadow:
      enabled: true
      color: "black"
      radius: 3
      offset: [ 1, 1 ]

```

## Description of Options
- **label:** The format string for the active window title. You can use placeholders like `{win[title]}` to dynamically insert window information.
- **label_alt:** The alternative format string for the active window. Useful for displaying additional window details.
- **label_no_window:** The text to display when no window is active. If not specified, it defaults to an empty string.
- **label_icon:** A boolean indicating whether to display the window icon.
- **label_icon_size:** The size of the window icon in pixels. Must be between 12px and 24px.
- **max_length:** The maximum number of characters to display for the window title. If the title exceeds this length, it will be truncated.
- **max_length_ellipsis:** The string to append to truncated window titles.
- **monitor_exclusive:** A boolean indicating whether the widget should be exclusive to a single monitor.
- **ignore_window:** A dictionary specifying which windows to ignore. It contains three lists: classes, processes, and titles.
- **callbacks:** A dictionary specifying the callbacks for mouse events. The keys are `on_left`, `on_middle`, and `on_right`, and the values are the names of the callback functions.
- **container_padding**: Explicitly set padding inside widget container. Use this option to set padding inside the widget container. You can set padding for top, left, bottom and right sides of the widget container.
- **animation:** A dictionary specifying the animation settings for the widget. It contains three keys: `enabled`, `type`, and `duration`. The `type` can be `fadeInOut` and the `duration` is the animation duration in milliseconds.
- **container_shadow:** Container shadow options.
- **label_shadow:** Label shadow options.

## Example Style
```css
.active-window-widget {}
.active-window-widget .widget-container {}
.active-window-widget .widget-container .label {}
.active-window-widget .widget-container .label.alt {}
.active-window-widget .widget-container .icon {}
```
