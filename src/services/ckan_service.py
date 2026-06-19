import requests
from typing import Any, Dict, List
from ckanapi import RemoteCKAN, ValidationError, NotAuthorized
from src.core.config import settings

class CKANService:
    def __init__(self):
        # Sessão customizada para desabilitar o SSL
        session = requests.Session()
        session.verify = False 

        self.ckan = RemoteCKAN(
            settings.CKAN_URL,
            apikey=settings.CKAN_API_KEY,
            user_agent="portal-api",
            session=session  
        )

    def _execute(self, action: str, **kwargs) -> Any:
        """Helper to execute CKAN actions with consistent error handling."""
        try:
            method = getattr(self.ckan.action, action)
            return method(**kwargs)
        except (ValidationError, NotAuthorized) as e:
            return {"error": str(e), "type": "auth_validation_error"}
        except Exception as e:
            return {"error": str(e), "type": "unexpected_error"}

    # ============= 
    # ORGANIZAÇÕES 
    # =============

    def listar_organizacoes(self) -> List[Dict]:
        """Lista todas as organizações com detalhes."""
        return self._execute("organization_list", all_fields=True)

    def criar_organizacao(self, **dados) -> Dict:
        """Cria uma nova organização."""
        return self._execute("organization_create", **dados)

    def obter_organizacao(self, org_id: str) -> Dict:
        """Busca detalhes de uma organização específica."""
        return self._execute("organization_show", id=org_id)

    def atualizar_organizacao(self, **dados) -> Dict:
        """Atualiza dados de uma organização existente."""
        return self._execute("organization_update", **dados)

    def excluir_organizacao(self, org_id: str) -> Dict:
        """Remove uma organização."""
        return self._execute("organization_delete", id=org_id)

    # ====================
    # CONJUNTOS DE DADOS
    # ==================== 

    def listar_datasets(self) -> Dict:
        """Lista conjuntos de dados (packages) incluindo privados."""
        return self._execute("package_search", include_private=True)

    def criar_dataset(self, **dados) -> Dict:
        """Cria um novo conjunto de dados."""
        return self._execute("package_create", **dados)

    def obter_dataset(self, dataset_id: str) -> Dict:
        """Busca detalhes de um conjunto de dados."""
        return self._execute("package_show", id=dataset_id)
    
    def atualizar_dataset(self, **dados) -> Dict:
        """Atualiza um conjunto de dados."""
        return self._execute("package_update", **dados)

    def excluir_dataset(self, dataset_id: str) -> Dict:
        """Remove um conjunto de dados."""
        return self._execute("package_delete", id=dataset_id)

    # ===============
    # RECURSOS / ARQUIVOS
    # ===============

    def listar_resources_dataset(self, dataset_id: str) -> List[Dict]:
        """Lista todos os recursos de um conjunto de dados específico."""
        dataset = self._execute("package_show", id=dataset_id)
        if isinstance(dataset, dict) and "error" in dataset:
            return []
        return dataset.get("resources", [])

    def criar_resources(self, **dados) -> Dict:
        """Adiciona um recurso (arquivo/link) a um dataset."""
        return self._execute("resource_create", **dados)

    def obter_resource(self, resource_id: str) -> Dict:
        """Busca detalhes de um recurso."""
        return self._execute("resource_show", id=resource_id)

    def atualizar_resource(self, **dados) -> Dict:
        """Atualiza um recurso existente."""
        return self._execute("resource_update", **dados)

    def excluir_resource(self, resource_id: str) -> Dict:
        """Remove um recurso."""
        return self._execute("resource_delete", id=resource_id)
    
    # ==============
    # GRUPOS
    # ==============

    def listar_grupos(self) -> List[Dict]:
        """Lista todos os grupos com detalhes."""
        return self._execute("group_list", all_fields=True)

    def obter_grupo(self, group_id: str) -> Dict:
        """Busca detalhes de um grupo específico."""
        return self._execute("group_show", id=group_id)

    def criar_grupo(self, **dados) -> Dict:
        """Cria um novo grupo."""
        return self._execute("group_create", **dados)

    def atualizar_grupo(self, **dados) -> Dict:
        """Atualiza um grupo existente."""
        return self._execute("group_update", **dados)
    
    def excluir_grupo(self, group_id: str) -> Dict:
        """Remove um grupo."""
        return self._execute("group_delete", id=group_id)
    
    # =================
    # TAGS
    # =================

    def listar_tags(self) -> List[str]:
        """Lista todas as tags cadastradas."""
        return self._execute("tag_list")

    def obter_tag(self, tag_id: str) -> Dict:
        """Busca detalhes de uma tag."""
        return self._execute("tag_show", id=tag_id)

    def buscar_datasets_por_tag(self, tag: str) -> Dict:
        """Lista datasets associados a uma tag."""
        return self._execute(
            "package_search",
            fq=f"tags:{tag}"
        )
    
    # ==================
    # Busca
    # ==================

    def buscar(self, termo: str, page: int = 1, limit: int = 20) -> Dict:
        """Buscar datasets no CKAN"""
        start = (page - 1) * limit

        return self._execute(
            "package_search",
            q=termo,
            rows=limit,
            start=start,
            include_private=True
        )
 

    # ==============
    # Upload de arquivos
    # ==============

    def upload_resource(
        self,
        package_id: str,
        file,
        name: str | None = None,
        description: str | None = None
    ):
        """Faz Upload de um arquivo para um dataset."""
        
        dados = {
            "package_id": package_id,
            "upload": file
        }

        if name:
            dados["name"] = name

        if description:
            dados["description"] = description

        return self._execute(
            "resource_create",
            **dados
        )
    
    # =================
    # Estatisticas
    # =================

    def obter_estatisticas(self) -> dict:

        datasets = self._execute(
            "package_search",
            rows=100,
            sort="metadata_modified desc",
            include_private=True
        )

        organizacoes = self._execute(
            "organization_list",
            all_fields=True
        )

        grupos = self._execute(
            "group_list"
        )

        tags = self._execute(
            "tag_list"
        )

        orgs_ativas = []

        for org in organizacoes[:5]:
            orgs_ativas.append({
                "nome": org["title"] if org.get("title") else org["name"],
                "datasets": org.get("package_count", 0)
            })

        orgs_ativas.sort(
            key=lambda x: x["datasets"],
            reverse=True
        )

        return {
            "total_datasets": datasets.get("count", 0),
            "total_organizacoes": len(organizacoes),
            "total_grupos": len(grupos),
            "total_tags": len(tags),

            "datasets_recentes": len(
                datasets.get("results", [])[:5]
            ),

            "organizacoes_mais_ativas": orgs_ativas[:5],

            "tags_populares": tags[:10]
        }

if __name__ == "__main__":
    service = CKANService()
    print(service.listar_organizacoes())