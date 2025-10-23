# Treasure Runner game code
self.game_over()


def game_over(self):
clear_screen()
print('GAME OVER')
print(f'Level: {self.level} Score: {self.score}')
name = input('Enter your name for the highscore table (or blank to skip): ').strip()
if name:
self.save_score(name)
print('Saved — thank you!')
else:
print('Score not saved.')
print('Highscores:')
self.print_highscores()
sys.exit(0)


def load_highscores(self):
try:
with open(HIGHSCORE_FILE, 'r') as f:
return json.load(f)
except Exception:
return []


def save_score(self, name):
self.highscores.append({'name': name, 'score': self.score, 'level': self.level, 'time': int(time.time())})
self.highscores = sorted(self.highscores, key=lambda x: x['score'], reverse=True)[:10]
with open(HIGHSCORE_FILE, 'w') as f:
json.dump(self.highscores, f)


def print_highscores(self):
for i, s in enumerate(self.highscores[:10], start=1):
t = time.strftime('%Y-%m-%d', time.localtime(s['time']))
print(f"{i}. {s['name']} — {s['score']} pts (Lv {s['level']}) {t}")


def mainloop(self):
while True:
self.draw()
key = read_key()
if not key:
continue
if key in ('q', 'Q'):
print('Quitting — thanks for playing!')
sys.exit(0)
if key in ('w', 'up'):
self.move_player(0, -1)
elif key in ('s', 'down'):
self.move_player(0, 1)
elif key in ('a', 'left'):
self.move_player(-1, 0)
elif key in ('d', 'right'):
self.move_player(1, 0)
# monsters move every turn
self.move_monsters()
self.turns += 1




def write_readme():
content = """
# Treasure Runner


A tiny terminal roguelite made with Python. Collect treasure, avoid monsters, reach the exit. Great for showcasing on GitHub and GitHub Sponsors.


## Run
```
python treasure_runner.py
```


Controls: WASD or arrow keys, Q to quit.


License: MIT
"""
with open('README.md', 'w', encoding='utf-8') as f:
f.write(content)
print('README.md written')




def main():
parser = argparse.ArgumentParser()
parser.add_argument('--write-readme', action='store_true', help='Write README.md to disk')
args = parser.parse_args()
if args.write_readme:
write_readme()
return
game = Game()
try:
game.mainloop()
except KeyboardInterrupt:
print('\nGoodbye!')


if __name__ == '__main__':
main()