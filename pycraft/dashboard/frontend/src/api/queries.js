import { useQuery } from '@tanstack/react-query';
import { fetchApi } from './client';

export function useServerInfo() {
  return useQuery({
    queryKey: ['server', 'info'],
    queryFn: () => fetchApi('/server/info'),
    staleTime: 60_000,
  });
}

export function useWorlds() {
  return useQuery({
    queryKey: ['server', 'worlds'],
    queryFn: () => fetchApi('/server/worlds'),
    staleTime: 60_000,
  });
}

export function usePlayers() {
  return useQuery({
    queryKey: ['players'],
    queryFn: () => fetchApi('/players'),
    staleTime: 5_000,
    refetchInterval: 10_000,
  });
}

/** Returns just the online players array for map/editor use */
export function useOnlinePlayers() {
  const { data, ...rest } = usePlayers();
  const online = data?.online || (Array.isArray(data) ? data : []);
  return { data: online, ...rest };
}

export function usePlayerDetail(uuid) {
  return useQuery({
    queryKey: ['players', uuid],
    queryFn: () => fetchApi(`/players/${uuid}`),
    staleTime: 5_000,
    enabled: !!uuid,
  });
}

export function usePlayerInventory(uuid) {
  return useQuery({
    queryKey: ['players', uuid, 'inventory'],
    queryFn: () => fetchApi(`/players/${uuid}/inventory`),
    staleTime: 10_000,
    enabled: !!uuid,
  });
}

export function useWorldEntities(worldName) {
  return useQuery({
    queryKey: ['worlds', worldName, 'entities'],
    queryFn: () => fetchApi(`/worlds/${worldName}/entities`),
    staleTime: 10_000,
    enabled: !!worldName,
  });
}

export function useWorldBlocks(worldName, params) {
  return useQuery({
    queryKey: ['worlds', worldName, 'blocks', params],
    queryFn: () => {
      const qs = new URLSearchParams(params).toString();
      return fetchApi(`/worlds/${worldName}/blocks?${qs}`);
    },
    staleTime: 30_000,
    enabled: !!worldName && !!params,
  });
}

export function useEnchantments() {
  return useQuery({
    queryKey: ['enchantments'],
    queryFn: () => fetchApi('/enchantments'),
    staleTime: 300_000, // cache for 5 min, enchantments don't change
  });
}

export function useApplicableEnchantments(uuid, slot) {
  return useQuery({
    queryKey: ['players', uuid, 'inventory', slot, 'applicable-enchantments'],
    queryFn: () => fetchApi(`/players/${uuid}/inventory/${slot}/applicable-enchantments`),
    staleTime: 30_000,
    enabled: !!uuid && slot != null,
  });
}

export function usePotionTypes() {
  return useQuery({
    queryKey: ['potion-types'],
    queryFn: () => fetchApi('/potion-types'),
    staleTime: 300_000,
  });
}

export function useTemplates() {
  return useQuery({
    queryKey: ['templates'],
    queryFn: () => fetchApi('/templates'),
    staleTime: 60_000,
  });
}

export function useTemplateDetail(name) {
  return useQuery({
    queryKey: ['templates', name],
    queryFn: () => fetchApi(`/templates/${encodeURIComponent(name)}`),
    staleTime: 60_000,
    enabled: !!name,
  });
}

export function useSearchBlocks(query) {
  return useQuery({
    queryKey: ['search', 'blocks', query],
    queryFn: () => fetchApi(`/search/blocks?q=${encodeURIComponent(query)}`),
    staleTime: 60_000,
    enabled: query?.length >= 1,
  });
}

export function useSearchEntities(query) {
  return useQuery({
    queryKey: ['search', 'entities', query],
    queryFn: () => fetchApi(`/search/entities?q=${encodeURIComponent(query)}`),
    staleTime: 60_000,
    enabled: query?.length >= 2,
  });
}

export function useMapSearch(query, world, x, z) {
  return useQuery({
    queryKey: ['search', 'map', query, world, x, z],
    queryFn: () => fetchApi(
      `/search/map?q=${encodeURIComponent(query)}&world=${encodeURIComponent(world)}&x=${x}&z=${z}`
    ),
    staleTime: 30_000,
    enabled: query?.length >= 2 && !!world,
  });
}
