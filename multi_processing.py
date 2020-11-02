from multiprocessing import Pool
import time

CONTADOR = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    pool = Pool(processes=2)
    inicio = time.time()
    pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f"Tempo em segundos: {fim - inicio}")

    # Tempo em segundos: 1.6009814739227295
