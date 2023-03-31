from rich.console import Console
console = Console(width=50)
console.rule(":leafy_green: Wyrdl :leafy_green:")
console.print("Hello, [bold red]Rich[/] :snake:")
console.print("[bold italic yellow on red blink]This text is impossible to read")
console.print("[bold]Bold[italic] bold and italic [/bold]italic[/italic]")
console.print(":warning-emoji:")
console.print(":warning:")
console.print(":red_heart-emoji:")
console.print(":red_heart:")

def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

print(rgb_to_hex
(255, 165, 1))

for x in ['#ff3366', 'white', '#ffffff', '#f5f000']:
    style = f'bold on {x}'
    msg = '  world!'
    console.print(f'[{style}] {msg}[/]')

for x in range(255):
    style = f'on {rgb_to_hex(255,0,x)}'
    msg = ' '
    console.print(f'[{style}] {msg}[/]', end='')