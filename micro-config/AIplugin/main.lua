local micro = import('micro')
local config = import('micro/config')
local shell = import('micro/shell')

function onBufferOpen(bp)
	config.MakeCommand("gemini", Gemini, config.NoComplete)
end

function Gemini(bp, args)
    local commandArgs = {}
    
	local request = shell.ExecCommand('cgemini', '-r', args[1])
    bp.Buf:Insert(-bp.Cursor.Loc, request)

    --bp:InsertNewline()
    --micro.InfoBar():Message(args[1])
end
