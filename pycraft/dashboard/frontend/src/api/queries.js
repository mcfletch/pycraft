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
