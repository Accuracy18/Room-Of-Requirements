-- import('micro')
-- config = import('micro/config')
-- shell = import('micro/shell')
-- local util = import('micro/util')
-- 
-- function onBufferOpen(bp)
--     config.MakeCommand("gemini", Gemini, config.NoComplete)
-- end
-- 
-- function Gemini(bp, args)
--     local cursor = bp.Cursor
--     local selection = cursor:GetSelection()
--     selection = util.String(selection)
--     local prompt = ""
-- 
--     if cursor:HasSelection() then
--         prompt = selection
--         -- micro.InfoBar():Message(5)
--     else
--         prompt = args[1]
--         micro.InfoBar():Message(6)
--     end
-- 
--     local request = shell.ExecCommand('python3', '/home/jojo/.config/micro/plug/AIplugin/gemini.py', '-r', prompt)
-- 
--     -- Find the line below the last comment
--     local line_num = cursor.Loc.Y
--     local last_comment_line = line_num
--     local buf = bp.Buf
-- 
--     for i = line_num, buf:Len() do
--         local line_text = buf:Line(i)
--         if line_text:match("^%s*--") then -- Check for leading spaces and "--"
--             last_comment_line = i
--         else
--             break -- Stop when the first non-comment line is found
--         end
--     end
-- 
--     -- Insert the new line after the last comment
--     bp.Buf:Insert({last_comment_line + 1, 1}, request)
--     micro.InfoBar():Message(selection)
--     --bp:InsertNewLine() -- Removed this line
-- end


local micro = import('micro')
local config = import('micro/config')
local shell = import('micro/shell')
local util = import('micro/util')

function onBufferOpen(bp)
	config.MakeCommand("gemini", Gemini, config.NoComplete)
end

function Gemini(bp, args)
    cursor = bp.Cursor
            
    selection = cursor:GetSelection()

    selection = util.String(selection)

    local prompt = ""
    
    if cursor:HasSelection() then
        prompt = selection

    else
        prompt = args[1]
    end
    
	local request = shell.ExecCommand('python3', '/home/jojo/.config/micro/plug/AIplugin/gemini.py', '-r', prompt)

    -- bp:InsertNewline()
    bp.Buf:Insert(-bp.Cursor.Loc, request)
    
    --micro.InfoBar():Message(selection)
    
end
