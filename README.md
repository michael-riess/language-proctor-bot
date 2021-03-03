# Language Proctor Bot

<p align="center">
    <img width="200" src="./assets/avatar.png"></img>
</p>
<p align="center">
    <span style="font-size:32px;"> 🇬🇧 🇺🇸 - 🇪🇸 🇲🇽 - 🇰🇷 </span>
</p>

A simple bot for maintaining language conformity in discord channels. Useful for language learning servers or just ensuring everyone understands what is being said.

<img width="600" src="https://user-images.githubusercontent.com/35740174/109806858-87b28a00-7c68-11eb-8e83-9f9360c00372.png"></img>

## Getting Started

*⚠️TODO: add directions for creating bot⚠️*

## Examples

1. Let's have Proctor Bot monitor for English use in the current channel.
```
$proctor-bot set-language en
```
<img width="400" src="https://user-images.githubusercontent.com/35740174/109813992-61ddb300-7c71-11eb-8d07-113f25057465.gif"></img>

2. When someone uses a different language Proctor Bot makes a gentle reminder to follow the channel language rules.

<img width="400" src="https://user-images.githubusercontent.com/35740174/109814547-fc3df680-7c71-11eb-9aa0-4e8b19f9d1ae.gif"></img>

3. Oops, we set language restrictions on the wrong channel, lets remove them.
```
$proctor-bot set-language none
```
<img width="400" src="https://user-images.githubusercontent.com/35740174/109819664-a8361080-7c77-11eb-841e-88cd896e0aaa.gif"></img>


## Commands
**All commands must be prefaced with ```$proctor-bot```.**
| command | arguments | effect | example |
|---|---|---|---|
| `set-language` | ISO 639 language code | sets channel language | `$proctor-bot set-language es` |


## Supported Languages
⚠️ ISO 639-1, 639-2, & 639-3 codes are all treated as 639-1, so there is no individual dialect support at this time.
- English
- Spanish (Español)
- Korean (한국어)

*Additional languages can and will be added as necessary.*

*If you are interested in contributing translations, those languages can be added.*


## Contributors
[<img alt="Michael Riess" src="https://avatars3.githubusercontent.com/u/35740174?s=460&v=4" width="117">](https://github.com/mriess260) |
:---:
|[Michael Riess](https://github.com/michael-riess)|
