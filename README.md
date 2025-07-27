# 📡 Sistema de Controle de Acesso e Registro de Presença com IoT

Projeto desenvolvido na disciplina de **Sistemas de IoT** do Instituto Federal do Paraná (IFPR), com o objetivo de implementar uma solução inteligente e segura para controle de acesso e registro de presença utilizando tecnologias como **RFID**, **ESP32** e **LoRa**.

## 🎯 Objetivo

Desenvolver um sistema de controle de acesso baseado em autenticação por RFID e comunicação sem fio com LoRa, possibilitando:

- Registro automático da presença de usuários.
- Autorização de acesso com resposta em tempo real.
- Monitoramento remoto através de um dashboard app.
- Envio de notificações via celular.

---

## 🧩 Componentes do Sistema

### 🔌 Hardware

- **ESP32**: Microcontrolador principal responsável pela leitura RFID e comunicação inicial.
- **ESP32 LoRa**: Gateway para transmitir dados via protocolo LoRa para o servidor.
- **Leitor RFID (MFRC522 ou PN532)**: Realiza a leitura dos tags RFID.
- **Tags RFID**: Cartões ou chaveiros com identificador único.
- **Smartphone Android/iOS**: Utilizado como hotspot e interface de notificação.
- **Fonte de alimentação (Powerbank ou fixa)**: Para alimentar os dispositivos.
- **Display OLED ou LEDs (opcional)**: Indicação visual do status (acesso permitido/negado).

### 💻 Software

- **Firmware ESP32 / ESP32 LoRa** (Arduino IDE ou MicroPython):
  - Comunicação entre dispositivos.
  - Envio de dados via HTTP/MQTT.
  - Requisição e recepção da autorização de acesso.

- **Dashboard App**:
  - Visualização de registros de acesso em tempo real.
  - Gerenciamento de usuários autorizados.

- **Banco de Dados**:
  - Armazena as chaves RFID dos usuários.
  - Registra eventos de autenticação (data, hora, dispositivo, usuário).

- **Notificações Push**:
  - Envio de alertas por PWA, Telegram ou WhatsApp.

---

## ⚙️ Funcionamento do Sistema

1. O usuário aproxima sua tag RFID do leitor.
2. O ESP32 envia o código lido para o ESP32 LoRa via comunicação local.
3. O ESP32 LoRa encaminha os dados ao servidor web.
4. O servidor:
   - Registra a presença.
   - Atualiza o dashboard.
   - Envia notificação ao celular.
   - Retorna a resposta (permitido/negado).
5. O ESP32 LoRa retransmite a resposta ao ESP32 original.
6. O ESP32, então:
   - Libera o acesso (caso autorizado) ou bloqueia (caso negado).
   - Exibe o status localmente via LEDs ou display.

---

## 👨‍💻 Equipe

Este projeto foi desenvolvido em equipe durante as aulas da disciplina. Cada integrante foi responsável por uma parte da implementação.
- [Ageu Felipe Nunes Moraes](https://github.com/Ageu-Felipe-Nunes-Moraes) - Banco de Dados
- [André Luiz Cecato Justus](https://github.com/andrececato) - API
- [Ciro Guilherme Nass](https://github.com/CiroGN) - frontend
- [Gabriel Alves Netto](https://github.com/alvesGabs) - hardware e firmware
- [Marjorie Ap. Cortez Daenecke](https://github.com/MarjorieDaenecke) - backend

---

## 🚀 Como Executar

1. Conecte os dispositivos ESP32 e leitores RFID conforme o circuito.
2. Carregue o firmware nos microcontroladores (ESP32 e ESP32 LoRa).
3. Configure o servidor web e banco de dados.
4. Inicie o dashboard web para visualizar os acessos.
5. Faça testes aproximando tags RFID conhecidas.

---

## 📎 Licença

Este projeto é de uso educacional, sem fins lucrativos, desenvolvido para fins de aprendizado e experimentação em IoT.

