# ABSTRAÇÃO

from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def log(self, msg):
        raise NotImplementedError("Implemente o método log")

    def log_error(self, msg):
        return self.log(f"ERROR: {msg}")

    def log_success(self, msg):
        return self.log(f"SUCCESS: {msg}")

class LogFileMixin(Log):
    def log(self, msg):
        msg_importada = f"{msg} ({self.__class__.__name__})"
        print("Salvando..", msg_importada)
        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(msg_importada)
            arquivo.write("\r\n")

class LogPrintMixin(Log):
    def log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")

if __name__ == "__main__":
    l = LogPrintMixin()
    l.log_error('Qualquer coisa')
    l.log_success('Qualquer coisa')

    lb = LogFileMixin()
    lb.log_error('Qualquer coisa')
    lb.log_success('Qualquer coisa')