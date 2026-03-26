import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import {
  AppBar,
  Box,
  Drawer,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography,
  Chip,
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import DnsIcon from '@mui/icons-material/Dns';
import PeopleIcon from '@mui/icons-material/People';
import ListAltIcon from '@mui/icons-material/ListAlt';
import MapIcon from '@mui/icons-material/Map';
import CodeIcon from '@mui/icons-material/Code';
import SearchIcon from '@mui/icons-material/Search';
import PetsIcon from '@mui/icons-material/Pets';
import LogoutIcon from '@mui/icons-material/Logout';
import { useServerInfo } from '../../api/queries';
import { useAuth } from '../../hooks/useAuth';

const DRAWER_WIDTH = 240;

const NAV_ITEMS = [
  { label: 'Map', icon: <MapIcon />, path: '/' },
  { label: 'Players', icon: <PeopleIcon />, path: '/players' },
  { label: 'Events', icon: <ListAltIcon />, path: '/events' },
  { label: 'Editor', icon: <CodeIcon />, path: '/editor' },
  { label: 'Search', icon: <SearchIcon />, path: '/search' },
  { label: 'Entities', icon: <PetsIcon />, path: '/entities' },
  { label: 'Server', icon: <DnsIcon />, path: '/server' },
];

function isActive(itemPath, currentPath) {
  if (itemPath === '/') return currentPath === '/' || currentPath === '/map';
  return currentPath.startsWith(itemPath);
}

export default function AppShell({ children, sseConnected }) {
  const [drawerOpen, setDrawerOpen] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const { data: serverInfo } = useServerInfo();
  const { username, logout } = useAuth();

  const drawer = (
    <Box sx={{ mt: 8 }}>
      <List>
        {NAV_ITEMS.map((item) => (
          <ListItem key={item.path} disablePadding>
            <ListItemButton
              selected={isActive(item.path, location.pathname)}
              onClick={() => {
                navigate(item.path);
                setDrawerOpen(false);
              }}
            >
              <ListItemIcon>{item.icon}</ListItemIcon>
              <ListItemText primary={item.label} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );

  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <IconButton
            color="inherit"
            edge="start"
            onClick={() => setDrawerOpen(!drawerOpen)}
            sx={{ mr: 2, display: { md: 'none' } }}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap sx={{ flexGrow: 1 }}>
            Pycraft Dashboard
          </Typography>
          {serverInfo?.mc_server && (
            <Typography variant="body2" sx={{ mr: 2, opacity: 0.8 }}>
              {serverInfo.mc_server}
            </Typography>
          )}
          <Chip
            label={sseConnected ? 'Live' : 'Disconnected'}
            color={sseConnected ? 'success' : 'error'}
            size="small"
            variant="outlined"
          />
          {username && (
            <Chip
              label={username}
              size="small"
              variant="outlined"
              onDelete={logout}
              deleteIcon={<LogoutIcon />}
              sx={{ ml: 1, color: 'inherit', borderColor: 'rgba(255,255,255,0.5)' }}
            />
          )}
        </Toolbar>
      </AppBar>

      {/* Mobile drawer */}
      <Drawer
        variant="temporary"
        open={drawerOpen}
        onClose={() => setDrawerOpen(false)}
        sx={{
          display: { xs: 'block', md: 'none' },
          '& .MuiDrawer-paper': { width: DRAWER_WIDTH },
        }}
      >
        {drawer}
      </Drawer>

      {/* Desktop drawer */}
      <Drawer
        variant="permanent"
        sx={{
          display: { xs: 'none', md: 'block' },
          '& .MuiDrawer-paper': { width: DRAWER_WIDTH },
        }}
        open
      >
        {drawer}
      </Drawer>

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          mt: 8,
          ml: { md: `${DRAWER_WIDTH}px` },
          height: 'calc(100vh - 64px)',
          overflow: 'auto',
          display: 'flex',
          flexDirection: 'column',
        }}
      >
        {children}
      </Box>
    </Box>
  );
}
