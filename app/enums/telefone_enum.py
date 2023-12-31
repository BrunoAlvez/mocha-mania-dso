from enum import Enum


class TelefoneEnum(Enum):
    DDD_SAO_PAULO_SP = 11
    DDD_SAO_JOSE_DOS_CAMPOS_SP = 12
    DDD_SANTOS_SP = 13
    DDD_BAURU_SP = 14
    DDD_SOROCABA_SP = 15
    DDD_RIBEIRAO_PRETO_SP = 16
    DDD_SAO_JOSE_DO_RIO_PRETO_SP = 17
    DDD_PRESIDENTE_PRUDENTE_SP = 18
    DDD_CAMPINAS_SP = 19
    DDD_RIO_DE_JANEIRO_RJ = 21
    DDD_CAMPOS_DOS_GOYTACAZES_RJ = 22
    DDD_VOLTA_REDONDA_RJ = 24
    DDD_VITORIA_ES = 27
    DDD_CACHOEIRO_DE_ITAPEMIRIM_ES = 28
    DDD_BELO_HORIZONTE_MG = 31
    DDD_JUIZ_DE_FORA_MG = 32
    DDD_GOVERNADOR_VALADARES_MG = 33
    DDD_UBERLANDIA_MG = 34
    DDD_POCOS_DE_CALDAS_MG = 35
    DDD_DIVINOPOLIS_MG = 37
    DDD_MONTES_CLAROS_MG = 38
    DDD_CURITIBA_PR = 41
    DDD_PONTA_GROSSA_PR = 42
    DDD_LONDRINA_PR = 43
    DDD_MARINGA_PR = 44
    DDD_FOZ_DO_IGUACU_PR = 45
    DDD_FRANCISCO_BELTRAO_PR = 46
    DDD_JOINVILLE_SC = 47
    DDD_FLORIANOPOLIS_SC = 48
    DDD_CHAPECO_SC = 49
    DDD_PORTO_ALEGRE_RS = 51
    DDD_PELOTAS_RS = 53
    DDD_CAXIAS_DO_SUL_RS = 54
    DDD_SANTA_MARIA_RS = 55
    DDD_BRASILIA_DF = 61
    DDD_GOIANIA_GO = 62
    DDD_PALMAS_TO = 63
    DDD_RIO_VERDE_GO = 64
    DDD_CUIABA_MT = 65
    DDD_RONDONOPOLIS_MT = 66
    DDD_CAMPO_GRANDE_MS = 67
    DDD_RIO_BRANCO_AC = 68
    DDD_PORTO_VELHO_RO = 69
    DDD_SALVADOR_BA = 71
    DDD_ILHEUS_BA = 73
    DDD_JUAZEIRO_BA = 74
    DDD_FEIRA_DE_SANTANA_BA = 75
    DDD_BARREIRAS_BA = 77
    DDD_ARACAJU_SE = 79
    DDD_RECIFE_PE = 81
    DDD_MACEIO_AL = 82
    DDD_JOAO_PESSOA_PB = 83
    DDD_NATAL_RN = 84
    DDD_FORTALEZA_CE = 85
    DDD_TERESINA_PI = 86
    DDD_PETROLINA_PE = 87
    DDD_JUAZEIRO_DO_NORTE_CE = 88
    DDD_PICOS_PI = 89
    DDD_BELEM_PA = 91
    DDD_MANAUSE_AM = 92
    DDD_SANTAREM_PA = 93
    DDD_MARABA_PA = 94
    DDD_BOA_VISTA_RR = 95
    DDD_MACAPA_AP = 96
    DDD_COARI_AM = 97
    DDD_SAO_LUIS_MA = 98
    DDD_IMPERATRIZ_MA = 99

    @staticmethod
    def ddds() -> list:
        return [ddd.value for ddd in TelefoneEnum]

    @staticmethod
    def digitos_adicionais() -> list[int]:
        return [9]
